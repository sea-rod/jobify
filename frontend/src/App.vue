 <!-- 
  Copyright 2025 Seamus.F.Rodrigues

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License. -->

<template>
    <!-- Navbar -->
    <nav class="bg-white shadow-md fixed w-full top-0 z-10">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
        <div class="text-2xl font-bold text-blue-600">Jobfiy</div>
        <div class="hidden md:flex space-x-8">
          <a href="#home" class="text-gray-700 hover:text-blue-600">Home</a>
          <a href="/upload-resume" class="text-gray-700 hover:text-blue-600">Upload Resume</a>
          <a href="#about" class="text-gray-700 hover:text-blue-600">About</a>
          <a href="#contact" class="text-gray-700 hover:text-blue-600">Contact</a>
        </div>
        <a v-if="isAuth" href="/auth" class="text-white bg-blue-500 px-5 py-2 hover:text-blue-600">Login</a>
        <a v-else="isAuth" href="#" class="text-white bg-red-500 px-5 py-2 hover:text-gray-200">Logout</a>

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
import { supabase } from "./supabase"

const isMenuOpen = ref(false)

const isAuth = ref(false)

isAuth.value = supabase.auth.user?true:false

function toggleMenu() {
  isMenuOpen.value = !isMenuOpen.value
}
</script>