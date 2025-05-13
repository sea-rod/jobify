<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="max-w-md w-full mx-auto bg-white rounded-lg shadow-lg p-8">
      <!-- Tabs -->
      <div class="flex justify-center mb-6">
        <button 
          @click="activeTab = 'signup'" 
          :class="{'bg-blue-600 text-white': activeTab === 'signup', 'bg-gray-200 text-gray-700': activeTab !== 'signup'}" 
          class="w-1/2 py-3 rounded-l-lg font-semibold transition duration-300"
        >
          Signup
        </button>
        <button 
          @click="activeTab = 'login'" 
          :class="{'bg-blue-600 text-white': activeTab === 'login', 'bg-gray-200 text-gray-700': activeTab !== 'login'}" 
          class="w-1/2 py-3 rounded-r-lg font-semibold transition duration-300"
        >
          Login
        </button>
      </div>

      <!-- Signup Form -->
      <div v-if="activeTab === 'signup'" class="space-y-6 animate-fade-in">
        <div>
          <label for="signup-name" class="block text-gray-700 font-medium mb-2">Full Name</label>
          <div class="relative">
            <i class="fas fa-user absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
            <input 
              v-model="signupForm.name" 
              type="text" 
              id="signup-name" 
              placeholder="John Doe" 
              class="w-full pl-10 p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              :class="{ 'border-red-500': signupErrors.name }"
            >
          </div>
          <p v-if="signupErrors.name" class="text-red-500 text-sm mt-1">{{ signupErrors.name }}</p>
        </div>

        <div>
          <label for="signup-email" class="block text-gray-700 font-medium mb-2">Email</label>
          <div class="relative">
            <i class="fas fa-envelope absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
            <input 
              v-model="signupForm.email" 
              type="email" 
              id="signup-email" 
              placeholder="john@example.com" 
              class="w-full pl-10 p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              :class="{ 'border-red-500': signupErrors.email }"
            >
          </div>
          <p v-if="signupErrors.email" class="text-red-500 text-sm mt-1">{{ signupErrors.email }}</p>
        </div>

        <div>
          <label for="signup-password" class="block text-gray-700 font-medium mb-2">Password</label>
          <div class="relative">
            <i class="fas fa-lock absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
            <input 
              v-model="signupForm.password" 
              type="password" 
              id="signup-password" 
              placeholder="••••••••" 
              class="w-full pl-10 p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              :class="{ 'border-red-500': signupErrors.password }"
            >
          </div>
          <p v-if="signupErrors.password" class="text-red-500 text-sm mt-1">{{ signupErrors.password }}</p>
        </div>

        <button 
          @click="handleSignup" 
          class="w-full bg-blue-600 text-white py-3 rounded-lg font-semibold hover:bg-blue-700 transition duration-300"
        >
          Sign Up
        </button>
      </div>

      <!-- Login Form -->
      <div v-if="activeTab === 'login'" class="space-y-6 animate-fade-in">
        <div>
          <label for="login-email" class="block text-gray-700 font-medium mb-2">Email</label>
          <div class="relative">
            <i class="fas fa-envelope absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
            <input 
              v-model="loginForm.email" 
              type="email" 
              id="login-email" 
              placeholder="john@example.com" 
              class="w-full pl-10 p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              :class="{ 'border-red-500': loginErrors.email }"
            >
          </div>
          <p v-if="loginErrors.email" class="text-red-500 text-sm mt-1">{{ loginErrors.email }}</p>
        </div>

        <div>
          <label for="login-password" class="block text-gray-700 font-medium mb-2">Password</label>
          <div class="relative">
            <i class="fas fa-lock absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
            <input 
              v-model="loginForm.password" 
              type="password" 
              id="login-password" 
              placeholder="••••••••" 
              class="w-full pl-10 p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              :class="{ 'border-red-500': loginErrors.password }"
            >
          </div>
          <p v-if="loginErrors.password" class="text-red-500 text-sm mt-1">{{ loginErrors.password }}</p>
        </div>

        <button 
          @click="handleLogin" 
          class="w-full bg-blue-600 text-white py-3 rounded-lg font-semibold hover:bg-blue-700 transition duration-300"
        >
          Log In
        </button>

        <div class="text-center">
          <a href="#" class="text-blue-600 hover:underline text-sm">Forgot Password?</a>
        </div>
      </div>

      <!-- Success/Error Messages -->
      <div v-if="message" class="mt-4 text-center" :class="messageType === 'success' ? 'text-green-600' : 'text-red-600'">
        {{ message }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import router from '../router'
import { supabase } from '../supabase' // Import your Supabase client

// Reactive state
const activeTab = ref('signup')

const signupForm = ref({
  name: '', 
  email: '',
  password: ''
})

const loginForm = ref({
  email: '',
  password: ''
})

const signupErrors = ref({
  name: '',
  email: '',
  password: ''
})

const loginErrors = ref({
  email: '',
  password: ''
})

const message = ref('')
const messageType = ref('')

// Helper function
const validateEmail = (email) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)

// Signup handler
const handleSignup = async () => {
  signupErrors.value = { name: '', email: '', password: '' }
  message.value = ''

  let isValid = true
  if (!signupForm.value.name) {
    signupErrors.value.name = 'Name is required'
    isValid = false
  }
  if (!signupForm.value.email) {
    signupErrors.value.email = 'Email is required'
    isValid = false
  } else if (!validateEmail(signupForm.value.email)) {
    signupErrors.value.email = 'Invalid email format'
    isValid = false
  }
  if (!signupForm.value.password) {
    signupErrors.value.password = 'Password is required'
    isValid = false
  } else if (signupForm.value.password.length < 8) {
    signupErrors.value.password = 'Password must be at least 8 characters'
    isValid = false
  }

  if (!isValid) return

  try {
    // Using Supabase to sign up the user
    const { user, error } = await supabase.auth.signUp({
      email: signupForm.value.email,
      password: signupForm.value.password,
      options: {
      data: {
        name: signupForm.value.name,
      }
    }
    })

    if (error) {
      throw error
    }

    message.value = 'Signup successful! Please log in.'
    messageType.value = 'success'
    activeTab.value = 'login'
    signupForm.value = { name: '', email: '', password: '' }
  } catch (error) {
    message.value = error.message
    messageType.value = 'error'
  }
}

// Login handler
const handleLogin = async () => {
  loginErrors.value = { email: '', password: '' }
  message.value = ''

  let isValid = true
  if (!loginForm.value.email) {
    loginErrors.value.email = 'Email is required'
    isValid = false
  } else if (!validateEmail(loginForm.value.email)) {
    loginErrors.value.email = 'Invalid email format'
    isValid = false
  }
  if (!loginForm.value.password) {
    loginErrors.value.password = 'Password is required'
    isValid = false
  }

  if (!isValid) return

  try {
    // Using Supabase to log in the user
    const { user, error } = await supabase.auth.signInWithPassword({
      email: loginForm.value.email,
      password: loginForm.value.password
    })

    if (error) {
      throw error
    }

    message.value = 'Login successful!'
    messageType.value = 'success'
    loginForm.value = { email: '', password: '' }
    router.push('/')
  } catch (error) {
    message.value = error.message
    messageType.value = 'error'
  }
}
</script>

<style scoped>
/* Tailwind CSS is already included in the parent app, so we only add scoped styles if needed */
.animate-fade-in {
  animation: fadeIn 0.3s ease-in;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>
