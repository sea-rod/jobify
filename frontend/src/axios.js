// api.js
import axios from 'axios';
import { supabase } from './supabase';  // Supabase client
import { useRouter } from 'vue-router';  // For redirection (make sure to install if using Vue Router)

const api = axios.create({
  baseURL: ' http://127.0.0.1:8000',
});

let currentUser = null;
let currentToken = null;
const router = useRouter(); // Vue Router for redirecting to login

// Function to get the current user and their token (stored by Supabase)
const fetchUserToken = async () => {
  const user = supabase.auth.user();
  if (user) {
    currentToken = user.access_token; // Supabase provides the token directly
    currentUser = user;
  } else {
    currentToken = null;
  }
};

// Listen for user state changes (login/logout)
supabase.auth.onAuthStateChange((event, session) => {
  if (session) {
    currentUser = session.user;
    currentToken = session.access_token;
  } else {
    currentUser = null;
    currentToken = null;
  }
});

// Function to refresh token
const refreshTokenIfNeeded = async () => {
  try {
    if (!currentToken) {
      throw new Error('No token found'); // No token, user needs to log in
    }

    // Refresh token by Supabase method
    const { data, error } = await supabase.auth.refreshSession();
    if (error) throw new Error('Failed to refresh token');
    
    // Successfully refreshed the token
    currentToken = data.session.access_token;
    return currentToken;
  } catch (error) {
    // Catch token errors (expired, missing, or refresh errors)
    console.error('Token error:', error.message);
    router.push('/login'); // Redirect to login if token is missing or refresh failed
    throw error; // Re-throw to handle request rejection
  }
};

// Interceptor to include the token in each request
api.interceptors.request.use(async (config) => {
  if (!currentToken) {
    await fetchUserToken(); // If no token, fetch the user token
  }
  if (currentToken) {
    config.headers.Authorization = `Bearer ${currentToken}`;
  }
  return config;
}, (error) => Promise.reject(error));

// Interceptor to catch 401 errors (token expired or invalid)
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response) {
      // Handle 401 errors (Unauthorized)
      if (error.response.status === 401) {
        console.log('Token expired or invalid, attempting to refresh...');
        try {
          // Attempt to refresh the token
          const token = await refreshTokenIfNeeded();
          
          // Retry the original request with the new token
          if (token) {
            error.config.headers.Authorization = `Bearer ${token}`;
            return axios(error.config);  // Retry the request
          }
        } catch (err) {
          // If refresh fails, redirect to login
          router.push('/login');
        }
      }
    }
    return Promise.reject(error);
  }
);

export default api;
