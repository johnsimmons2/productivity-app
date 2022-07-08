const { injectManifest } = require('workbox-build')
const path = require('path')

const workboxConfig = require('./workbox-config')
console.log('Configuration: ', workboxConfig)

injectManifest(workboxConfig).then(({count, size}) => {
    console.log(`Generated ${workboxConfig.swDest}, which will cache ${count} files (${size} byes)`)
})