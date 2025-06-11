# The project steps :



1 - Setting up a local postgreSQL server using a Docker container

2 - Implementing a Python script that retrieves two datasets for September 2024 and stores the retrieved data in two SQL tables within a postgreSQL database

3 - Writing an SQL query that aggregates the aFRR volumes up and down from 1min to 15min granularity and stores the result in a third SQL table

4 - Writing an SQL query that calculates, for the day 05/09/2024, the revenue in € from the aFRR up and down markets using the 15min imbalance price and the aggregated data from the previous step.


### Setting Up a Local PostgreSQL Server with Docker in Google Colab


## 1️⃣ Installing Docker

Start by installing Docker Desktop by downloading the software from the link below:


🔗 [Install Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/)

## 2️⃣ Creating a Docker Account
After installing Docker Desktop, you can create a Docker account using your email via the following link:


🔗 [Create a Docker Account](https://login.docker.com/u/login/)

## 3️⃣ Logging into Docker 
To authenticate with Docker Hub, run the following command and enter your credentials:

```sh
docker login
```

## 4️⃣ Running a PostgreSQL Container
Run the following command to start a PostgreSQL container:

```sh
docker run --name test-project -e POSTGRES_PASSWORD=testpass -p 5432:5432 -d postgres
```

### 🛠 Explanation of Parameters:
- `--name test-project` → Names the container "test-project"
- `-e POSTGRES_PASSWORD=testpass` → Sets the PostgreSQL user password
- `-p 5432:5432` → Maps local port 5432 to the PostgreSQL container
- `-d postgres` → Runs the container in the background using the PostgreSQL image

## 5️⃣ Verifying the Running Container
To check if the PostgreSQL container is running, execute:

```sh
docker ps
```

## 6️⃣ Stopping and Removing the Container
To stop and remove the container when done:

```sh
docker stop test-project
docker rm test-project

