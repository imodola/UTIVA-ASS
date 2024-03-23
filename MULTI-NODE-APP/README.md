# MULTI NODE JS CONFIG
### Stage 1: Build the application
FROM node:latest AS builder

### Set working directory in the container
WORKDIR /app

### Copy package.json and package-lock.json to container
COPY package*.json ./

### Install dependencies
RUN npm install

### Copy the application code
COPY . .

### Build the application
RUN npm run build

### Stage 2: Create the final lightweight image
FROM node:slim AS runtime

### Set working directory in the container
WORKDIR /app

### Copy the built application from the builder stage
COPY --from=builder /app .

### Expose port
EXPOSE 3000

### Command to run the application
CMD ["npm", "start"]
