import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    host: true,      // listen on all interfaces
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://cloudmart-backend:8000',  // backend container
        changeOrigin: true,
        secure: false,
      },
    },
  },
});
