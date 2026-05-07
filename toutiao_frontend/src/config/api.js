// API基础URL配置
export const apiConfig = {
  // 后端API基础URL
  baseURL: 'http://127.0.0.1:8000',
}

// AI配置 - 不再直接请求阿里云，而是请求自己的后端代理
export const aiChatConfig = {
  apiEndpoint: 'http://127.0.0.1:8000/api/ai/chat',
  // apiKey 和 model 已移到后端，前端不再管理
}