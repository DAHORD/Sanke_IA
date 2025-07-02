# snake_project/model.py

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os
from settings import MODEL_PATH, HIDDEN_LAYER_SIZE

class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x

    def save(self, data_to_save):
        model_folder_path = os.path.dirname(MODEL_PATH)
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)
        torch.save(data_to_save, MODEL_PATH)

class QTrainer:
    # On réintroduit le target_model pour le Double DQN
    def __init__(self, model, target_model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.target_model = target_model
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()

    def train_step(self, state, action, reward, next_state, done):
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)
        if len(state.shape) == 1:
            state = torch.unsqueeze(state, 0)
            next_state = torch.unsqueeze(next_state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            done = (done, )

        pred = self.model(state)
        target = pred.clone()
        for idx in range(len(done)):
            Q_new = reward[idx]
            if not done[idx]:
                # --- LOGIQUE DOUBLE DQN ---
                next_pred = self.model(next_state[idx])
                best_action_idx = torch.argmax(next_pred).item()
                q_value_from_target = self.target_model(next_state[idx])[best_action_idx]
                Q_new = reward[idx] + self.gamma * q_value_from_target
            
            action_idx = torch.argmax(action[idx]).item()
            target[idx][action_idx] = Q_new
    
        self.optimizer.zero_grad()
        loss = self.criterion(target, pred)
        loss.backward()
        self.optimizer.step()