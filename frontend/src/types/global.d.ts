// src/types/global.d.ts
export {};

declare global {
  interface Window {
    accessToken: string;
    user_id: string;
  }
}
