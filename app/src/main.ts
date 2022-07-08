import { enableProdMode, NgZone } from '@angular/core';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/app.module';
import { environment } from './environments/environment';
import { Workbox } from "workbox-window";

if (environment.production) {
  enableProdMode();
}

function loadServiceWorker(ngZone: NgZone) {
  if ('serviceworker' in navigator) {
    const wb = new Workbox('/sw.js');
    navigator.serviceWorker.addEventListener('sw-message', event => {
      ngZone.run(() => {
        console.log('Received message ', event.target)
      });
    });

    wb.register().then(result => {
      if (result?.active?.state !== 'activated') {
        return;
      }
    });
  }
}

platformBrowserDynamic()
  .bootstrapModule(AppModule)
  .then(moduleRef => {
    const ngZone = moduleRef.injector.get(NgZone);

    loadServiceWorker(ngZone);
  })
  .catch(err => console.error(err));

