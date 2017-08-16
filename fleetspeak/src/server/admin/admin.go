// Copyright 2017 Google Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Package admin defines an administrative interface into the fleetspeak system.
package admin

import (
	"bytes"
	"errors"
	"fmt"

	"context"

	"github.com/google/fleetspeak/fleetspeak/src/common"
	"github.com/google/fleetspeak/fleetspeak/src/server/db"

	fspb "github.com/google/fleetspeak/fleetspeak/src/common/proto/fleetspeak"
	spb "github.com/google/fleetspeak/fleetspeak/src/server/proto/fleetspeak_server"
	sgrpc "github.com/google/fleetspeak/fleetspeak/src/server/proto/fleetspeak_server"
)

// NewServer returns an admin_grpc.AdminServer which performs operations using
// the provided db.Store.
func NewServer(s db.Store) sgrpc.AdminServer {
	return adminServer{s}
}

type adminServer struct {
	store db.Store
}

func (s adminServer) CreateBroadcast(ctx context.Context, req *spb.CreateBroadcastRequest) (*fspb.EmptyMessage, error) {
	if err := s.store.CreateBroadcast(ctx, req.Broadcast, req.Limit); err != nil {
		return nil, err
	}
	return &fspb.EmptyMessage{}, nil
}

func (s adminServer) ListActiveBroadcasts(ctx context.Context, req *spb.ListActiveBroadcastsRequest) (*spb.ListActiveBroadcastsResponse, error) {
	var ret spb.ListActiveBroadcastsResponse
	bis, err := s.store.ListActiveBroadcasts(ctx)
	if err != nil {
		return nil, err
	}
	for _, bi := range bis {
		if req.ServiceName != "" && req.ServiceName != bi.Broadcast.Source.ServiceName {
			continue
		}
		ret.Broadcasts = append(ret.Broadcasts, bi.Broadcast)
	}
	return &ret, nil
}

func (s adminServer) GetMessageStatus(ctx context.Context, req *spb.GetMessageStatusRequest) (*spb.GetMessageStatusResponse, error) {
	mid, err := common.BytesToMessageID(req.MessageId)
	if err != nil {
		return nil, err
	}

	msgs, err := s.store.GetMessages(ctx, []common.MessageID{mid}, false)
	if err != nil {
		if s.store.IsNotFound(err) {
			return &spb.GetMessageStatusResponse{}, nil
		}
		return nil, err
	}
	if len(msgs) != 1 {
		return nil, fmt.Errorf("Internal error, expected 1 message, got %d", len(msgs))
	}

	return &spb.GetMessageStatusResponse{
			CreationTime: msgs[0].CreationTime,
			Result:       msgs[0].Result},
		nil
}

func (s adminServer) ListClients(ctx context.Context, _ *fspb.EmptyMessage) (*spb.ListClientsResponse, error) {
	clients, err := s.store.ListClients(ctx)
	if err != nil {
		return nil, err
	}

	return &spb.ListClientsResponse{
		Clients: clients,
	}, nil
}

// InsertMessage implements sgrpc.AdminServer.
func (s adminServer) InsertMessage(ctx context.Context, m *fspb.Message) (*fspb.EmptyMessage, error) {
	// At this point, we mostly trust the message we get, but do some basic
	// sanity checks and generate missing metadata.
	if m.Destination == nil || m.Destination.ServiceName == "" {
		return nil, errors.New("message must have Destination")
	}
	if m.Source == nil || m.Source.ServiceName == "" {
		return nil, errors.New("message must have Source")
	}
	if len(m.MessageId) == 0 {
		id, err := common.RandomMessageID()
		if err != nil {
			return nil, fmt.Errorf("unable to create random MessageID: %v", err)
		}
		m.MessageId = id.Bytes()
	}
	if m.CreationTime == nil {
		m.CreationTime = db.NowProto()
	}
	if err := s.store.StoreMessages(ctx, []*fspb.Message{m}, ""); err != nil {
		return nil, err
	}
	return &fspb.EmptyMessage{}, nil
}

// StoreFile implements sgrpc.AdminServer.
func (s adminServer) StoreFile(ctx context.Context, req *spb.StoreFileRequest) (*fspb.EmptyMessage, error) {
	if req.ServiceName == "" || req.FileName == "" {
		return nil, errors.New("file must have service_name and file_name")
	}
	if err := s.store.StoreFile(ctx, req.ServiceName, req.FileName, bytes.NewReader(req.Data)); err != nil {
		return nil, err
	}
	return &fspb.EmptyMessage{}, nil
}

// KeepAlive implements sgrpc.AdminServer.
func (s adminServer) KeepAlive(ctx context.Context, _ *fspb.EmptyMessage) (*fspb.EmptyMessage, error) {
	return &fspb.EmptyMessage{}, nil
}