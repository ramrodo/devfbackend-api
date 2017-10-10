run:
	docker build -t docker-api-devf .
	docker-compose up
clean:
	docker ps -a | grep Exit | cut -d ' ' -f 1 | xargs docker rm
	docker rmi docker-api-devf
	#docker images | grep none | awk '{print $3}' | xargs docker rmi

