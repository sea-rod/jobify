import { createClient } from '@supabase/supabase-js'

// Replace with your Supabase project URL and anon/public key
const SUPABASE_URL = import.meta.env.VITE_SUPABASE_URL
const SUPABASE_KEY = import.meta.env.VITE_SUPABASE_KEY
export const supabase = createClient(SUPABASE_URL, SUPABASE_KEY)
