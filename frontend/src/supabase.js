import { createClient } from '@supabase/supabase-js'

// Replace with your Supabase project URL and anon/public key
const SUPABASE_URL = import.meta.env.VITE_SUPABASE_URL
const SUPABASE_KEY = import.meta.env.VITE_SUPABASE_KEY
console.log(SUPABASE_URL,"kk");

export const supabase = createClient(SUPABASE_URL, SUPABASE_KEY)
