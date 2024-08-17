# Use an official Node.js image as the base image
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json from the react-app directory
COPY react-app/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the React app code to the working directory
COPY react-app ./
# Expose the port the app will run on
EXPOSE 3000

# Command to run the React app
CMD ["npm", "start"]
