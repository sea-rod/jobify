// composables/useAuth.js
import { ref, readonly, onMounted,computed } from 'vue'
import { supabase } from '@/supabase'

const user = ref(null)

const initAuth = async () => {
  const { data } = await supabase.auth.getUser()
  user.value = data.user?true:false

  supabase.auth.onAuthStateChange((_event, session) => {
    user.value = session?.user?true:false    
  })
}
export function useAuth() {
  onMounted(() => {
    initAuth()
  })

  const isAuth = computed(() =>user.value)

  return {
    user: readonly(user),
    isAuth: isAuth
  }
}
