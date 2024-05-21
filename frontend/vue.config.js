// vue.config.js
module.exports = {
    publicPath: process.env.NODE_ENV === 'production'
      ? '/deepsky/'
      : '/'
    configureWebpack: {
      resolve: {
        alias: {
          '@': require('path').resolve(__dirname, 'src')
        }
    },
    plugins: [
      new (require('webpack')).DefinePlugin({
        '__VUE_OPTIONS_API__': JSON.stringify(true),
        '__VUE_PROD_DEVTOOLS__': JSON.stringify(false),
        '__VUE_PROD_HYDRATION_MISMATCH_DETAILS__': JSON.stringify(false)
      })
    ]
  }
};
