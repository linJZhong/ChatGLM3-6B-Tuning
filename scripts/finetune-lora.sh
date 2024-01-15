python finetune-lora.py \
    --dataset_path data/processed_datas.jsonl \
    --lora_rank 8 \
    --per_device_train_batch_size 6 \
    --gradient_accumulation_steps 1 \
    --max_steps 52000 \
    --save_steps 1000 \
    --save_total_limit 2 \
    --learning_rate 1e-4 \
    --fp16 \
    --remove_unused_columns false \
    --logging_steps 50 \
    --output_dir output
    --chatglm_path model_path/chat_glm3 #更改为自己本地的model path