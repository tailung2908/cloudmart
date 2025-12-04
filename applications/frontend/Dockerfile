# Stage 1: Build
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy all source files including Vite config
COPY vite.config.js ./
COPY ./src ./src
COPY index.html ./

# Stage 2: Run dev server
# If you want production build, you would run `npm run build` here
CMD ["npm", "run", "dev", "--", "--host"]
EXPOSE 5173
