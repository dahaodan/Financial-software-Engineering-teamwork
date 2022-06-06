"use strict";
const path = require("path");
const defaultSettings = require("./src/settings.js");

function resolve(dir) {
  return path.join(__dirname, dir);
}

const name = defaultSettings.title || "firstapp"; // page title
const port = process.env.port || process.env.npm_config_port || 8080; // dev port

// All configuration item explanations can be find in https://cli.vuejs.org/config/
module.exports = {
  chainWebpack(config) {
    // set svg-sprite-loader
    config.module;
    rule("svg")
      .exclude.add(resolve("src/assets/icons"))
      .end();
    config.module
      .rule("icons")
      .test(/\.svg$/)
      .include.add(resolve("src/assets/icons"))
      .end()
      .use("svg-sprite-loader")
      .loader("svg-sprite-loader")
      .options({
        symbolId: "icon-[name]"
      })
      .end();
  }
};
