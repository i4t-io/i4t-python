PACKAGE = i4t
INCLUDE = .:$(PBOSE_PROTOBUF_PATH)

.PHONY: lint

lint: check-env
	protoc --lint_out=. -I$(INCLUDE) $(PACKAGE)/protobuf/*.proto

check-env:
ifndef PBOSE_PROTOBUF_PATH
  $(error PBOSE_PROTOBUF_PATH is undefined)
endif
