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
     <section id="home" class="min-h-screen flex items-center justify-center gradient-bg text-white pt-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-4xl md:text-6xl font-bold mb-4 animate-fade-in">Land Your Dream Job with jobify</h1>
        <p class="text-lg md:text-xl mb-8">Upload your CV, optimize it for ATS, and get tailored job recommendations effortlessly.</p>
        <button class="bg-white text-blue-600 px-6 py-3 rounded-full font-semibold hover:bg-blue-100 transition duration-300">Get Started</button>
      </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl md:text-4xl font-bold text-center text-gray-800 mb-12">Why Choose jobify?</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <!-- Feature 1 -->
          <div class="bg-gray-50 p-6 rounded-lg shadow-md hover:shadow-lg transition duration-300">
            <i class="fas fa-file-upload text-blue-600 text-4xl mb-4"></i>
            <h3 class="text-xl font-semibold text-gray-800 mb-2">Easy CV Upload</h3>
            <p class="text-gray-600">Drag and drop your CV to securely save and manage it within jobify.</p>
          </div>
          <!-- Feature 2 -->
          <div class="bg-gray-50 p-6 rounded-lg shadow-md hover:shadow-lg transition duration-300">
            <i class="fas fa-check-circle text-blue-600 text-4xl mb-4"></i>
            <h3 class="text-xl font-semibold text-gray-800 mb-2">ATS Optimization</h3>
            <p class="text-gray-600">Get a checklist to make your CV ATS-friendly and download the optimized version.</p>
          </div>
          <!-- Feature 3 -->
          <div class="bg-gray-50 p-6 rounded-lg shadow-md hover:shadow-lg transition duration-300">
            <i class="fas fa-briefcase text-blue-600 text-4xl mb-4"></i>
            <h3 class="text-xl font-semibold text-gray-800 mb-2">Smart Job Recommendations</h3>
            <p class="text-gray-600">Receive job suggestions tailored to your CV, with auto-updated applications.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section id="about" class="py-20 bg-gray-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl md:text-4xl font-bold text-gray-800 mb-6">About jobify</h2>
        <p class="text-gray-600 max-w-2xl mx-auto">jobify is designed to simplify your job search. From CV optimization to personalized job recommendations, we help you stand out and land the job you deserve.</p>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl md:text-4xl font-bold text-gray-800 mb-6">Get in Touch</h2>
        <p class="text-gray-600 mb-8">Have questions? Reach out to us, and we’ll get back to you soon.</p>
        <div class="max-w-md mx-auto">
          <input type="email" placeholder="Your Email" class="w-full p-3 mb-4 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600">
          <textarea placeholder="Your Message" class="w-full p-3 mb-4 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600" rows="4"></textarea>
          <button class="bg-blue-600 text-white px-6 py-3 rounded-full font-semibold hover:bg-blue-700 transition duration-300">Send Message</button>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white py-6">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <p>&copy; 2025 jobify. All rights reserved.</p>
        <div class="mt-4 flex justify-center space-x-4">
          <a href="#" class="hover:text-blue-400"><i class="fab fa-twitter"></i></a>
          <a href="#" class="hover:text-blue-400"><i class="fab fa-linkedin"></i></a>
          <a href="#" class="hover:text-blue-400"><i class="fab fa-github"></i></a>
        </div>
      </div>
    </footer>
</template>