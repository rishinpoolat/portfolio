import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface ChatMessage {
  message: string;
}

export interface ChatResponse {
  response: string;
  sources: Array<{
    file_name: string;
    relevance_score: number;
    content: string;
  }>;
  suggested_questions: string[];
  session_id: string;
  response_time: number;
}

export interface ApiStats {
  total_documents: number;
  total_chunks: number;
  categories: Record<string, number>;
  health_status: string;
}

export const apiService = {
  async sendChatMessage(message: string, sessionId?: string): Promise<ChatResponse> {
    const response = await apiClient.post('/chat', {
      message,
      session_id: sessionId,
    });
    return response.data;
  },

  async getStats(): Promise<ApiStats> {
    const response = await apiClient.get('/stats');
    return response.data;
  },

  async getHealth(): Promise<{ status: string }> {
    const response = await apiClient.get('/health');
    return response.data;
  },

  async refreshDatabase(): Promise<{ message: string }> {
    const response = await apiClient.post('/refresh');
    return response.data;
  },
};

export default apiService;