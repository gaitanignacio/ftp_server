## USAGE
cd FTP_SERVER
docker build  -t ftp_server . -f ./Dockerfile
docker run -it --rm -p 21:21 -p 30000-30010:30000-30010 -v $PWD/FILES:/usr/local/src/ftp_server/jetson ftp_server