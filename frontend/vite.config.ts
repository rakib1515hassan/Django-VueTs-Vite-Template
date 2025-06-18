import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";
import { fileURLToPath, URL } from "node:url";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],

  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
      "@dashboard": path.resolve(__dirname, "../../apps/dashboard/assets/js"),
      vue: "vue/dist/vue.esm-bundler.js",
    },
    extensions: [".ts", ".js", ".vue", ".json"],
  },

  css: {
    postcss: "./postcss.config.js",
    preprocessorOptions: {
      scss: {
        additionalData: `@import "@/assets/scss/variables.scss";`,
      },
    },
  },

  build: {
    outDir: path.resolve(__dirname, "../static/vue"),
    emptyOutDir: true,
    manifest: true,
    cssCodeSplit: false,
    assetsDir: "assets",
    rollupOptions: {
      input: path.resolve(__dirname, "src/main.ts"),
      output: {
        entryFileNames: "assets/[name].js",
        chunkFileNames: "assets/[name].js",
        assetFileNames: (assetInfo) => {
          if (assetInfo.name && /\.(css|scss|sass)$/.test(assetInfo.name)) {
            return "assets/css/[name].[ext]";
          }
          if (
            assetInfo.name &&
            /\.(png|jpe?g|gif|svg|webp|avif)$/.test(assetInfo.name)
          ) {
            return "assets/images/[name].[ext]";
          }
          if (
            assetInfo.name &&
            /\.(woff2?|eot|ttf|otf)$/.test(assetInfo.name)
          ) {
            return "assets/fonts/[name].[ext]";
          }
          return "assets/[name].[ext]";
        },
      },
    },
  },

  server: {
    host: "localhost",
    port: 5173,
    strictPort: true,
    hmr: {
      protocol: "ws",
      host: "localhost",
      port: 5173,
    },
    watch: {
      usePolling: true,
      interval: 100,
    },
  },

  optimizeDeps: {
    include: ["vue", "@vue/runtime-core", "@vue/shared"],
    exclude: ["vue-demi"],
  },
});
