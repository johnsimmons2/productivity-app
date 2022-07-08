import { precacheAndRoute } from 'workbox-precaching'

declare const self: ServiceWorkerGlobalScope;
const assets = self.__WB_MANIFEST;

precacheAndRoute(assets);