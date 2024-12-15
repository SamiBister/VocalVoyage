const nextTranslate = require("next-translate");

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  i18n: {
    locales: ['en', 'fi'],
    defaultLocale: 'en',
    localeDetection: true
  },
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
    level: 'info',
    fetches: {
      fullUrl: true
    }
  },
  // Enable detailed console output
  onDemandEntries: {
    maxInactiveAge: 25 * 1000,
    pagesBufferLength: 2,
  },
    // Remove the rewrites section since we're using i18n
  // Add middleware config for handling locales
  trailingSlash: false,
  // Preserve distDir and translation settings
  distDir: '.next',
  ...nextTranslate()
};



module.exports = nextConfig;