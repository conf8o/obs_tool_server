@echo off
curl -X PUT -H "Content-Type: application/json" http://localhost:8000/scene_section -d "{\"current_scene\": \"%~1\"}"