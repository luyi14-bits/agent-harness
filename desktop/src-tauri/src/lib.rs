use std::process::Command;

/// 列出所有已加载的 Agent（调用 Python CLI）
#[tauri::command]
fn list_skills(skill_dir: String) -> Result<String, String> {
    let output = Command::new("python")
        .args(["-m", "src.tree_sop_agent.cli.main", "--skill-dir", &skill_dir, "--list"])
        .output()
        .map_err(|e| e.to_string())?;
    Ok(String::from_utf8_lossy(&output.stdout).to_string())
}

/// 运行 SOP 管道（启动 Dispatcher）
#[tauri::command]
fn run_pipeline(prompt: String, skill_dir: String) -> Result<String, String> {
    let escaped_dir = skill_dir.replace("\\", "\\\\");
    let escaped_prompt = prompt.replace('\'', "\\'");
    let code = format!(
        r#"import sys; sys.path.insert(0,'.'); from tree_sop_agent.orchestrator.dispatcher import Dispatcher; d=Dispatcher(skill_dir='{}'); print(d.handle('{}'))"#,
        escaped_dir, escaped_prompt
    );
    let output = Command::new("python")
        .args(["-c", &code])
        .output()
        .map_err(|e| e.to_string())?;
    Ok(String::from_utf8_lossy(&output.stdout).to_string())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![list_skills, run_pipeline])
        .run(tauri::generate_context!())
        .expect("启动 Tree-SOP Agent 桌面应用失败");
}
