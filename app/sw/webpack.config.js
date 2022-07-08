const path = require("path");
const webpack = require("webpack");
const workboxWebpack = require('workbox-webpack-plugin');

module.exports = {
    target: "web",
    mode: "none",
    entry: './src/index.ts',
    module: {
        rules: [
            {
                test: /\.ts$/,
                exclude: /node_modules|e2e/,
                loader: 'ts-loader'
            }
        ]
    },
    resolve: {
        extensions: ['.ts', '.js']
    },
    output: {
        path: path.resolve(__dirname, 'build'),
        filename: 'sw.js'
    },
    plugins: [
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': JSON.stringify('development')
        })
    ]
};