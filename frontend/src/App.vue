<template>
    <!-- Navbar -->
    <nav class="bg-white shadow-md fixed w-full top-0 z-10">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
        <div class="text-2xl font-bold text-blue-600">Jobfiy</div>
        <div class="hidden md:flex space-x-8">
          <a href="#home" class="text-gray-700 hover:text-blue-600">Home</a>
          <a href="#features" class="text-gray-700 hover:text-blue-600">Features</a>
          <a href="#about" class="text-gray-700 hover:text-blue-600">About</a>
          <a href="#contact" class="text-gray-700 hover:text-blue-600">Contact</a>
        </div>
        <a href="/auth" class="text-white bg-blue-500 px-5 py-2 hover:text-blue-600">Login</a>
        <button class="md:hidden" @click="toggleMenu">
          <i class="fas fa-bars text-gray-700 text-2xl"></i>
        </button>
      </div>
      <!-- Mobile Menu -->
      <div v-if="isMenuOpen" class="md:hidden bg-white shadow-md">
        <div class="flex flex-col space-y-4 px-4 py-4">
          <a href="#home" class="text-gray-700 hover:text-blue-600" @click="toggleMenu">Home</a>
          <a href="#features" class="text-gray-700 hover:text-blue-600" @click="toggleMenu">Features</a>
          <a href="#about" class="text-gray-700 hover:text-blue-600" @click="toggleMenu">About</a>
          <a href="#contact" class="text-gray-700 hover:text-blue-600" @click="toggleMenu">Contact</a>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
     <router-view/>
   
</template>


<script setup>
import { ref } from "vue";

const isMenuOpen = ref(false)

function toggleMenu() {
  isMenuOpen.value = !isMenuOpen.value
}
</script>