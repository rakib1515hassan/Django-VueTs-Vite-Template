# Vue 3 + Vite 

## Project create

```bash
npm create vite@latest frontend -- --template vue
```
```bash
npm create vite@latest . -- --template vue
```


### use TypeScript
```bash
npm create vite@latest my-vue-app -- --template vue-ts
```
```bash
npm create vite@latest . -- --template vue-ts
```

### Stracture 

```bash
frontend/
├── node_modules/
├── public/
├── src/
│   ├── assets/
│   ├── components/
│   ├── App.vue
│   ├── style.css
│   └── main.js
├── index.html
├── package.json
├── vite.config.js
```


## vite.config.js

```bash
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

import path from "path";

import { fileURLToPath, URL } from "node:url";

// https://vite.dev/config/
export default defineConfig({
  // base: "/static/vue/", // এটা দিলে vue http://localhost:5173/static/vue/ এই ভাবে run হবে।

  plugins: [vue()],

  resolve: {
      alias: {
         "@": fileURLToPath(new URL("./src", import.meta.url)),
         vue: "vue/dist/vue.esm-bundler.js",
      },
  },

   css: {
      postcss: "./postcss.config.js",
   },

  build: {
      outDir: path.resolve(__dirname, "../static/vue"), // <-- output in Django static
      emptyOutDir: true,
      cssCodeSplit: false,
      assetsDir: "assets",
      manifest: true,
      rollupOptions: {
         input: path.resolve(__dirname, "src/main.js"),
         output: {
         entryFileNames: "assets/main.js",
         chunkFileNames: "assets/[name].js",
         assetFileNames: (assetInfo) => {
            if (assetInfo.name && assetInfo.name.endsWith(".css")) {
               return "assets/style.css";
            }
            return "assets/[name][extname]";
         },
         },
      },
  },
});

```



## main.js

```bash
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp({});

import { DashboardComponent } from "../../apps/auth/assets/js/app.js";
app.component("admin-dashboard", DashboardComponent);

app.mount("#app");
```



## index.html

```bash
{% load static %}
<!DOCTYPE html>
<html lang="en-US" dir="ltr">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %} Master {% endblock title %}</title>

    <!-- =========================================================================== -->
    <!-- ========================( Vue JS Connection )============================== -->
    <!--  -->
    {% if debug %}
    <!-- Vite Dev Server during development -->
    <script type="module" src="http://localhost:5173/@vite/client"></script>
    <script type="module" src="http://localhost:5173/src/main.js"></script>
    {% else %}
    <!-- Production build files -->
    <link rel="stylesheet" href="{% static 'vue/assets/style.css' %}">
    <script type="module" src="{% static 'vue/assets/main.js' %}"></script>
    {% endif %}
    <!-- =========================================================================== -->

    <meta name="csrf-token" content="{{ csrf_token }}">
    {% block styles %}{% endblock styles %}
</head>

<body>
    <div id="app">
        {% block content %}

        {% endblock content %}
    </div>
    {% block js %} {% endblock js %}
</body>

</html>
```



## To add Vue Router

```bash
npm install vue-router@4
```



## To add Pinia (state management):
```bash
npm install pinia
```



## npm Cache clean:
```bash
npm cache clean --force
```




# Tailwind CSS Install 

## 1. Install Tailwind CSS 

#### Using Vite
```base
npm install tailwindcss @tailwindcss/postcss postcss
```




## 2. Import Tailwind CSS

#### Add it on your vue style.css/main.css file
```base
@import "tailwindcss" source(none);

@source "../src/**/*.vue";
@source "../src/**/*.js";

@source "../../templates/**/*.html";
@source "../../**/templates/**/*.html";
@source "../../**/*.vue";
```




## 3. Setup tailwind.config.js

```base
export default {
    content: [
        './src/**/*.{js,vue}',
        '../templates/**/*.html',
    ],
    theme: {
        extend: {},
    },
    plugins: [],
};
```



## 4. Setup postcss.config.js

```base
export default {
    plugins: {
        "@tailwindcss/postcss": {},
    },
};
```



## 5. Configure the Vite vite.config.js plugin

```base
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

import path from "path";

import { fileURLToPath, URL } from "node:url";


// https://vite.dev/config/
export default defineConfig({
  // base: "/static/vue/", // এটা দিলে vue http://localhost:5173/static/vue/ এই ভাবে run হবে।

  plugins: [vue()],

  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
      vue: "vue/dist/vue.esm-bundler.js",
    },
  },

  css: {
    postcss: "./postcss.config.js",
  },

  build: {
    outDir: path.resolve(__dirname, "../static/vue"), // <-- output in Django static
    emptyOutDir: true,
    cssCodeSplit: false,
    assetsDir: "assets",
    manifest: true,
    rollupOptions: {
      input: path.resolve(__dirname, "src/main.js"),
      output: {
        entryFileNames: "assets/main.js",
        chunkFileNames: "assets/[name].js",
        assetFileNames: (assetInfo) => {
          if (assetInfo.name && assetInfo.name.endsWith(".css")) {
            return "assets/style.css";
          }
          return "assets/[name][extname]";
        },
      },
    },
  },
});
```





# Note: Tailwind Sugenst in VS Code Editor

#### VS Code এর settings.json ফাইলের files.associations এর "*html": "html", নিচের কনফিগারেশন যুক্ত করুন:

```base
"files.associations": {
  "*html": "html",
  "*.css": "tailwindcss"
},
```

#### VS Code এর settings.json ফাইলে নিচের কনফিগারেশন যুক্ত করুন:
```base
"tailwindCSS.includeLanguages": {
  "vue": "html"
},
"editor.quickSuggestions": {
  "strings": true
},
"editor.inlineSuggest.enabled": true
```





# Vue TypeScript Setup + Django

## 1. 