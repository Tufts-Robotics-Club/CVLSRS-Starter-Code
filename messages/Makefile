# brew install protobuf  (this command will install protoc, allowing you to compile the protobuf files)
protobuf: target.proto rotationCommand.proto tiltCommand.proto text.proto
	protoc -I=./ --python_out=./ ./target.proto
	protoc -I=./ --python_out=./ ./rotationCommand.proto
	protoc -I=./ --python_out=./ ./tiltCommand.proto
	protoc -I=./ --python_out=./ ./text.proto