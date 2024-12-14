const nextTranslate = require("next-translate");

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  experimental: {
    forceSwcTransforms: true
  },
  webpack: (config, { isServer }) => {
    if (!isServer) {
      config.devtool = 'source-map';
    }
    return config;
  },
  // Configure logging properly
  logging: {
    fetches: {
      fullUrl: false
    }
  },
  // Preserve distDir and translation settings
  distDir: '.next',
  ...nextTranslate()
};

module.exports = nextConfig;