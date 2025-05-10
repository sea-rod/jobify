<template>
    <div class="min-h-screen bg-gray-100 flex items-center justify-center py-10">
        <div class="max-w-4xl w-full mx-auto bg-white rounded-lg shadow-lg p-8">
            <!-- Header -->
            <h1 class="text-3xl font-bold text-gray-800 mb-6 text-center">Upload Your Resume</h1>

            <!-- Resume Upload Section (Shown initially) -->
            <div v-if="!isAnalyzed" class="mb-8">
                <div class="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center hover:border-blue-600 transition duration-300"
                    @dragover.prevent @drop.prevent="handleDrop">
                    <input type="file" id="resume-upload" accept=".pdf,.doc,.docx" class="hidden"
                        @change="handleFileUpload" :disabled="fileName !== null">
                    <label for="resume-upload" class="cursor-pointer"
                        :class="{ 'opacity-50 cursor-not-allowed': fileName }">
                        <i class="fas fa-file-upload text-blue-600 text-4xl mb-4"></i>
                        <p class="text-gray-600">Drag & drop your resume here or click to upload</p>
                        <p class="text-sm text-gray-500">Supported formats: PDF, DOC, DOCX (Max 5MB)</p>
                    </label>
                </div>

                <!-- Uploaded File Preview -->
                <div v-if="fileName" class="mt-4 flex items-center justify-center space-x-4">
                    <i class="fas fa-file-alt text-blue-600 text-2xl"></i>
                    <p class="text-gray-700">{{ fileName }}</p>
                    <button @click="removeFile" class="text-red-500 hover:text-red-700">
                        <i class="fas fa-trash-alt"></i>
                    </button>
                </div>
            </div>

            <!-- Analyze Button (Shown only after upload) -->
            <div v-if="!isUploaded" class="text-center mb-8">
                <button @click="uploadResume" :disabled="!fileName"
                    class="bg-blue-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-blue-700 transition duration-300 disabled:bg-gray-400 disabled:cursor-not-allowed">
                    Upload Resume
                </button>
            </div>
            <div v-if="!isAnalyzed && isUploaded" class="text-center mb-8">
                <button @click="analyzeResume" :disabled="!fileName"
                    class="bg-green-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-green-700 transition duration-300 disabled:bg-gray-400 disabled:cursor-not-allowed">
                    Analyze Resume
                </button>
            </div>

            <!-- Feedback Section (Replaces upload section after analysis) -->
            <div v-if="isAnalyzed" class="space-y-6">
                <h2 class="text-2xl font-semibold text-gray-800 text-center">ATS Optimization Feedback</h2>
                <div class="bg-gray-50 p-6 rounded-lg shadow-md">
                    <p class="text-gray-600 mb-4">Here’s what you can do to make your resume more ATS-friendly:</p>
                    <div v-for="(item, index) in feedback" :key="index" class="flex items-start space-x-3 mb-3">
                        <input type="checkbox" :id="'feedback-' + index" v-model="item.completed"
                            class="mt-1 h-5 w-5 text-blue-600 rounded">
                        <label :for="'feedback-' + index" class="text-gray-700">{{ item.suggestion }}</label>
                    </div>
                    <div class="text-center mt-6">
                        <button @click="applySuggestions" :disabled="!allFeedbackCompleted"
                            class="bg-green-600 text-white py-2 px-6 rounded-lg font-semibold hover:bg-green-700 transition duration-300 disabled:bg-gray-400 disabled:cursor-not-allowed">
                            Apply Suggestions
                        </button>
                    </div>
                </div>

                <!-- Download Option (Shown after applying suggestions) -->
                <div v-if="atsResumeGenerated" class="mt-4 text-center">
                    <button
                        class="bg-blue-600 text-white py-2 px-6 rounded-lg font-semibold hover:bg-blue-700 transition duration-300"
                        @click="downloadResume">
                        Download ATS-Friendly Resume
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref, computed } from 'vue';

// Reactive state
const fileName = ref(null);
const feedback = ref([]);
const isUploaded = ref(false);
const isAnalyzed = ref(false);
const atsResumeGenerated = ref(false);

// Handle file upload via input
const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
        validateAndSetFile(file);
    }
};

// Handle file drop
const handleDrop = (event) => {
    event.preventDefault(); // prevent default browser behavior
    const file = event.dataTransfer.files[0];
    if (file) {
        validateAndSetFile(file);
    }
};

// Validate and set uploaded file
const validateAndSetFile = (file) => {
    const allowedTypes = [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    ];
    const maxSize = 5 * 1024 * 1024; // 5MB

    if (!allowedTypes.includes(file.type)) {
        alert('Please upload a PDF, DOC, or DOCX file.');
        return;
    }
    if (file.size > maxSize) {
        alert('File size exceeds 5MB limit.');
        return;
    }

    fileName.value = file.name;
    feedback.value = [];
    isAnalyzed.value = false;
    isUploaded.value = false;
    atsResumeGenerated.value = false;
};

// Remove uploaded file
const removeFile = () => {
    fileName.value = null;
    feedback.value = [];
    isAnalyzed.value = false;
    atsResumeGenerated.value = false;
};

// Mock resume upload
const uploadResume = () => {
    isUploaded.value = !isUploaded.value;
};

// Mock analysis
const analyzeResume = () => {
    feedback.value = [
        { suggestion: 'Add relevant keywords from the job description.', completed: false },
        { suggestion: 'Use standard section headings like "Experience" and "Education".', completed: false },
        { suggestion: 'Remove complex formatting and graphics.', completed: false },
        { suggestion: 'Ensure consistent font sizes and styles.', completed: false },
        { suggestion: 'Include measurable achievements with numbers.', completed: false }
    ];
    isAnalyzed.value = true;
};

// Computed: check if all feedback is complete
const allFeedbackCompleted = computed(() => {
    return feedback.value.length > 0 && feedback.value.every(item => item.completed);
});

// Mock apply suggestions
const applySuggestions = () => {
    if (allFeedbackCompleted.value) {
        atsResumeGenerated.value = true;
    }
};

// Mock download
const downloadResume = () => {
    alert('Downloading ATS-friendly resume... (This is a mock action)');
};
</script>


<style scoped>
/* Tailwind CSS is already included in the parent app, so we only add scoped styles if needed */
</style>