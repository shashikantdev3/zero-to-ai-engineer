"""Zero to AI Engineer · Production and LLMOps · Part 7 of 38
Slide: The Lua script, part one
Run: python 01_the_lua_script_part_one.py
"""
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
