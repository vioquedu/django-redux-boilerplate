var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,

  entry: './index',

  output: {
      path: path.resolve('../static/bundle/'),
      filename: "[name]-[hash].js"
  },

  plugins: [
  ], // add all common plugins here

  module: {
    loaders: [
      {test: /\.css$/, loader: 'style-loader!css-loader'},
      {test: /\.(png|woff|woff2|eot|ttf|svg)(\?v=\d+\.\d+\.\d+)?$/, loader: 'url-loader?limit=100000' },
      {test: /\.js$/, loader: 'imports?jQuery=jquery,$=jquery,this=>window'}
    ] // add all common loaders here
  },

  resolve: {
    modulesDirectories: ['node_modules'],
    extensions: ['', '.js', '.jsx']
  },
}
