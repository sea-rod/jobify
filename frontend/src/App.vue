<template>
  <nav class="bg-white text-gray-700 fixed w-full top-0 z-50 shadow-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <!-- Logo -->
        <div class="flex items-center">
          <img src="./assets/icon.png" height="64px" width="64px">
          <span class="text-2xl font-bold text-blue-500">Jobify</span>
        </div>

        <!-- Desktop Menu -->
        <div class="hidden md:flex items-center space-x-8">
          <router-link 
            v-for="link in navLinks" 
            :key="link.name" 
            :to="link.path"
            class="hover:text-blue-500 transition-colors duration-200"
            active-class="text-blue-500"
          >
            {{ link.name }}
          </router-link>
          <router-link 
            v-if="!isAuth"
            to="/auth"
            class="px-4 py-2 bg-blue-500 text-white hover:bg-blue-600 rounded-md transition-colors duration-200"
          >
            Login
          </router-link>
          <button 
            v-else
            @click="signOut"
            class="px-4 py-2 bg-red-500 text-white hover:bg-red-600 rounded-md transition-colors duration-200"
          >
            Logout
          </button>
          <router-link 
            v-if="!isAuth"
            to="/signup"
            class="px-4 py-2 bg-green-500 text-white hover:bg-green-600 rounded-md transition-colors duration-200"
          >
            Signup
          </router-link>
        </div>

        <!-- Mobile Menu Button -->
        <div class="md:hidden flex items-center">
          <button 
            @click="toggleMenu" 
            class="focus:outline-none"
            aria-label="Toggle menu"
          >
            <svg 
              class="w-6 h-6 transition-transform duration-300 text-gray-700"
              :class="{ 'rotate-90': isMenuOpen }"
              fill="none" 
              stroke="currentColor" 
              viewBox="0 0 24 24"
            >
              <path 
                :d="!isMenuOpen ? 'M4 6h16M4 12h16M4 18h16' : 'M6 18L18 6M6 6l12 12'"
                stroke-linecap="round" 
                stroke-linejoin="round" 
                stroke-width="2"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Menu -->
    <transition 
      enter-active-class="transition-all duration-300 ease-in-out"
      leave-active-class="transition-all duration-300 ease-in-out"
      enter-from-class="clip-path-start"
      enter-to-class="clip-path-end"
      leave-from-class="clip-path-end"
      leave-to-class="clip-path-start"
    >
      <div v-if="isMenuOpen" class="md:hidden bg-white">
        <div class="px-2 pt-2 pb-3 space-y-1">
          <transition-group 
            enter-active-class="transition-all duration-300 ease-in-out"
            leave-active-class="transition-all duration-300 ease-in-out"
            enter-from-class="transform -translate-y-4 opacity-0"
            enter-to-class="transform translate-y-0 opacity-100"
            leave-from-class="transform translate-y-0 opacity-100"
            leave-to-class="transform -translate-y-4 opacity-0"
          >
            <router-link 
              v-for="link in navLinks" 
              :key="link.name" 
              :to="link.path"
              class="block px-3 py-2 text-base font-medium hover:bg-blue-100 rounded-md transition-colors duration-200"
              active-class="text-blue-500"
              @click="toggleMenu"
            >
              {{ link.name }}
            </router-link>
            <router-link 
              v-if="!isAuth"
              key="login"
              to="/auth"
              class="block px-3 py-2 text-base font-medium bg-blue-500 text-white hover:bg-blue-600 rounded-md transition-colors duration-200"
              @click="toggleMenu"
            >
              Login
            </router-link>
            <button 
              v-else
              key="logout"
              @click="signOut"
              class="block px-3 py-2 text-base font-medium bg-red-500 text-white hover:bg-red-600 rounded-md transition-colors duration-200"
            >
              Logout
            </button>
            <router-link 
              v-if="!isAuth"
              key="signup"
              to="/signup"
              class="block px-3 py-2 text-base font-medium bg-green-500 text-white hover:bg-green-600 rounded-md transition-colors duration-200"
              @click="toggleMenu"
            >
              Signup
            </router-link>
          </transition-group>
        </div>
      </div>
    </transition>
  </nav>
  <router-view/>
</template>

<script setup>
import { ref } from 'vue'
import { supabase } from './supabase'
import router from './router'

const isMenuOpen = ref(false)
const isAuth = ref(false)

const navLinks = [
  { name: 'Home', path: '/' },
  { name: 'Upload Resume', path: '/upload-resume' },
  { name: 'Jobs', path: '/jobs' },
  { name: 'Contact', path: '/contact' },
]

supabase.auth.getUser().then((res) => {
  console.log(res.data)
  isAuth.value = res.data.user ? true : false
})

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const signOut = () => {
  supabase.auth.signOut().then((res) => {
    console.log(res, 'logged out successfully')
    router.push('/')
    isAuth.value = false
  }).catch(err => {
    console.log(err)
  })
}
</script>

<style scoped>
nav {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.clip-path-start {
  clip-path: polygon(0 0, 0 0, 0 0, 0 0);
}

.clip-path-end {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
}
</style>