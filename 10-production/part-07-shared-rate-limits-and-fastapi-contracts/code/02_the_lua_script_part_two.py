"""Zero to AI Engineer · Production and LLMOps · Part 7 of 38
Slide: The Lua script, part two
Run: python 02_the_lua_script_part_two.py
"""
# --- repeated from 01_the_lua_script_part_one.py so this file runs on its own ---
LUA = """
local cap  = tonumber(ARGV[1])
local rate = tonumber(ARGV[2])
local cost = tonumber(ARGV[3])
local t = redis.call('TIME')
local now = tonumber(t[1])
  + tonumber(t[2]) / 1000000
local b = redis.call('HMGET', KEYS[1],
  'tokens', 'ts')
local tokens = tonumber(b[1]) or cap
local ts = tonumber(b[2]) or now
"""

# --- this slide ---
LUA += """
tokens = math.min(cap,
  tokens + (now - ts) * rate)
local allowed = 0
if tokens >= cost then
  tokens = tokens - cost; allowed = 1
end
redis.call('HSET', KEYS[1], 'tokens',
  tokens, 'ts', now)
redis.call('EXPIRE', KEYS[1],
  math.ceil(cap / rate) * 2)
return allowed"""
