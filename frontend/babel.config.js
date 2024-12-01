// babel.config.js
module.exports = {
  presets: [
    [
      '@babel/preset-react',
      {
        runtime: 'automatic', // Adds the new JSX transform
      },
    ],
    '@babel/preset-env',
  ],
};