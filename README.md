## Log-Monitor
This is the repository created to host the opensearch single node cluster on the local system. This uses docker desktop for building opensearch and dashboard container.


# Prerequisite
1. Install Docker Desktop using the appropriate distribution - https://www.docker.com/products/docker-desktop/
2. Make sure from settings Increase the resources RAM configuration to 6-8GB
3. Use the docker-compose.yml file to build 2 containers - opensearch & opensearch-dashboard.
4. `docker compose up -d`
<img width="555" height="113" alt="Screenshot 2026-01-09 at 09 31 24" src="https://github.com/user-attachments/assets/b1ed9dd9-8561-4a43-91ef-193c9ff8a051" />

5. Check the health of containers
<img width="1198" height="486" alt="Screenshot 2026-01-09 at 09 35 40" src="https://github.com/user-attachments/assets/00cef440-181b-43db-b5d0-7271989497c0" />
Note - yellow status is because index has 1 primary shard and 1 replica. Because of single node, replica wont get assigned.

6. Use script.py to ingest data to cluster
<img width="553" height="131" alt="Screenshot 2026-01-09 at 09 42 36" src="https://github.com/user-attachments/assets/26782343-e2ed-4569-856e-8c957bcd38fe" />


7. Once data is ingested. Create the index pattern in the opensearch dashboard. for below index
<img width="1065" height="207" alt="Screenshot 2026-01-09 at 09 45 23" src="https://github.com/user-attachments/assets/da2c8799-cd1f-4486-a94a-d0a85e42856d" />

8. Click on manage and then create index pattern
<img width="1431" height="720" alt="Screenshot 2026-01-09 at 09 47 27" src="https://github.com/user-attachments/assets/9476f116-3edf-4e15-9adc-dd941b0e35a5" />
<img width="1445" height="500" alt="Screenshot 2026-01-09 at 09 48 42" src="https://github.com/user-attachments/assets/85e2a500-3b74-4219-a6a8-26dbefbda596" />

9. Click on discover to see ingested data
<img width="1132" height="628" alt="Screenshot 2026-01-09 at 09 49 01" src="https://github.com/user-attachments/assets/aeef63ca-ae5d-4406-b88b-1bfbd837c9ad" />
<img width="1459" height="761" alt="Screenshot 2026-01-09 at 09 50 39" src="https://github.com/user-attachments/assets/745cce17-aed3-4724-9680-70fa50ded8c9" />

This completes end to end log monitoring pipeline using opensearch. different log forwarder agent can alos be used like logstash, filebeat fluentbit with this setup.
