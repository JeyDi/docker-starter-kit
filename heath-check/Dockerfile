version: '3.4'
services:
	redis:
		image: redis
		healthcheck:
			test: ["CMD","redis-cli","ping"]
			start_period: 30s
			interval: 15s
			timeout: 3s
			retries: 5