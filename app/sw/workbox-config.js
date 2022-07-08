module.exports = {
    globDirectory: "../dist/app/",
    globStrict: true,
    globIgnores: [
        "**/*-es5.*.js",
        "sw.js"
    ],
    // Don't match files cached by angular
    dontCacheBustURLsMatching: new RegExp(".+.[a-f0-9]{20}..+"),
    maximumFileSizeToCacheInBytes: 20 * 1024 * 1024, // 20MB
    swSrc: "build/sw.js",
    swDest: "../dist/app/sw.js"
};