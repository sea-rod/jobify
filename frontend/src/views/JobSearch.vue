<template>
    <div class="container mt-20 mx-auto px-4">
            <div class="flex flex-col md:flex-row gap-4 mb-6">
                <div class="flex-1">
                    <input 
                        type="text" 
                        placeholder="Search jobs..." 
                        class="w-full p-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
                    >
                </div>
                <div class="flex-1 md:flex-none">
                    <select class="w-full md:w-48 p-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500">
                        <option value="">Filter by Category</option>
                        <option value="tech">Technology</option>
                        <option value="marketing">Marketing</option>
                        <option value="finance">Finance</option>
                        <option value="design">Design</option>
                    </select>
                </div>
            </div>

            <!-- Job Listings -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div v-for="job in jobs" class="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
                    <h2 class="text-xl font-semibold text-blue-600">{{job.title}}</h2>
                    <p class="text-gray-600 mt-2">{{job.description}}</p>
                    <p class="text-gray-500 mt-2"><span class="font-medium">Location:</span>{{job.location}}</p>
                    <a v-bind:href="job.redirect_url">

                        <button class="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors">Apply Now</button>
                    </a>
                </div>

                
            </div>
        </div>
</template>


<script setup>
import api from '../axios';
import { ref,onMounted } from 'vue';

const jobs = ref([]);

import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";


onMounted(() => {
    api.get("/jobs").then(res=>{
        console.log(res);
        console.log(res.data);
        jobs.value = res.data
        
    }).catch((err)=>{
        toast(err.response.data.detail, {
          "theme": "auto",
          "type": "error",
          "dangerouslyHTMLString": true
        })
        console.log(err);
        
    })
})


</script>