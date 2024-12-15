console.log('API URL from env:', process.env.NEXT_PUBLIC_API_URL);
export const API_URL = process.env.NEXT_PUBLIC_API_URL || '/api';
console.log('Final API URL:', API_URL);