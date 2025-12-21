#!/usr/bin/env python3
import subprocess
import sys
import re

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.returncode == 0, result.stdout.strip(), result.stderr.strip()

def get_git_status():
    success, output, _ = run_command("git status --porcelain")
    return output.split('\n') if success and output else []

def extract_day_number(files):
    for file in files:
        match = re.search(r'Day - (\d+)', file)
        if match:
            return match.group(1)
    return None

def get_project_title(day_num):
    try:
        with open(f"Day - {day_num}/README.md", 'r') as f:
            for line in f:
                if line.startswith('# Day'):
                    title = line.strip().replace('# ', '')
                    return title
    except:
        pass
    return f"Day {day_num} Project"

def main():
    print("🔍 Checking git status...")
    files = get_git_status()
    if not files or files == ['']:
        print("❌ No changes to commit")
        return
    
    print(f"📁 Found {len(files)} changed files")
    for file in files[:5]:  # Show first 5 files
        print(f"   {file}")
    
    day_num = extract_day_number(files)
    if not day_num:
        print("❌ No Day directory found")
        return
    
    print(f"\n📂 Found Day {day_num} directory")
    
    # Commit 1: New Day directory
    print(f"\n🔄 Step 1: Adding Day - {day_num} directory...")
    success, stdout, stderr = run_command(f'git add "Day - {day_num}"')
    if success:
        print("✅ Day directory added")
        title = get_project_title(day_num)
        print(f"🔄 Committing: {title}")
        success, stdout, stderr = run_command(f'git commit -m "{title}"')
        if success:
            print(f"✅ Committed: {title}")
        else:
            print(f"❌ Commit failed: {stderr}")
    else:
        print(f"❌ Add failed: {stderr}")
    
    # Commit 2: README update
    print(f"\n🔄 Step 2: Committing README updates...")
    success, stdout, stderr = run_command('git commit -am "Day {day_num} progress updated"'.format(day_num=day_num))
    if success:
        print(f"✅ Committed: Day {day_num} progress updated")
    else:
        print(f"❌ README commit failed: {stderr}")
    
    # Push
    print("\n🔄 Step 3: Pushing to remote...")
    success, stdout, stderr = run_command("git push")
    if success:
        print("✅ Pushed to remote successfully")
    else:
        print(f"❌ Push failed: {stderr}")
    
    print("\n🎉 Git update process completed!")

if __name__ == "__main__":
    main()