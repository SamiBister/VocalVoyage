// .eslintrc.js
module.exports = {
  parser: '@babel/eslint-parser',
  extends: [
    'eslint:recommended',
    'plugin:react/recommended'
  ],
  plugins: ['react'],
  settings: {
    react: {
      version: 'detect'
    }
  },
  parserOptions: {
    ecmaVersion: 2020,
    sourceType: 'module',
    ecmaFeatures: {
      jsx: true
    }
  },
  rules: {
    'react/react-in-jsx-scope': 'off', // For React 17+ new JSX transform
    'no-unused-vars': ['error', { 
      varsIgnorePattern: 'React' 
    }]
  },
  overrides: [
    {
      files: ['**/*.test.js', '**/*.test.jsx', '**/__tests__/**/*.{js,jsx}'],
      rules: {
        'no-unused-vars': 'off',
        'react/react-in-jsx-scope': 'error' // Enforce React import in test files
      }
    }
  ]
};