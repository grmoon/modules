const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  devtool: 'source-map',
  mode: 'development',
  entry: path.resolve('src', 'js', 'index.js'),
  output: {
    path: path.resolve('dist'),
    filename: '[name].[hash].js'
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        exclude: /node_modules/,
        use: ['vue-loader', 'eslint-loader']
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['babel-loader', 'eslint-loader']
      },
      {
        test: /\.s?css$/,
        exclude: /node_modules/,
        use: ['style-loader', 'css-loader', 'postcss-loader', 'sass-loader']
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: path.resolve('src', 'html', 'index.html')
    }),
    new CleanWebpackPlugin(['dist'], {
      root: path.resolve()
    }),
    new VueLoaderPlugin()
  ],
  resolve: {
    alias: {
      '@components': path.resolve('src', 'components'),
      '@css': path.resolve('src', 'css'),
      '@js': path.resolve('src', 'js'),
      '@store': path.resolve('src', 'js', 'store')
    },
    extensions: ['.vue', '.js', '.css']
  }
}
