PACKAGE = i4t
PROTOBUF_INCLUDE = vendor/$(PACKAGE)-protobuf:$(PBOSE_PROTOBUF_PATH)

.PHONY: test protobuf clean

test:
	tox

protobuf: check-env
	protoc --python_out=. -I$(PROTOBUF_INCLUDE) vendor/$(PACKAGE)-protobuf/$(PACKAGE)/protobuf/*.proto

clean:
	rm $(PACKAGE)/protobuf/*_pb2.py

check-env:
ifndef PBOSE_PROTOBUF_PATH
  $(error PBOSE_PROTOBUF_PATH is undefined)
endif
