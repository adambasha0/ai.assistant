from django.shortcuts import render

from django.http import JsonResponse
from openai import OpenAI

client = OpenAI(api_key="add-your-key-here")


def chat_with_gpt(request):
    # Extract command from URL parameter 'command'
    command = request.GET.get('command', '')
    conversation_history = request.session.get('conversation_history', [])
    final_command = """use this api end point to fast generate molecule using chemotion apis, only modify the smiles given in the command:
    api end point: https://complat-eln.ioc.kit.edu/api/v1/molecules/smiles
    request payload: {smiles: "replace this string with actual smiles requested", editor: "ketcher"}
    only give me the new api end point with the modified request payload in the response"""
    final_command += f"\n{command}"
    # print (final_command)
    if not command:
        return JsonResponse({"error": "No command provided"}, status=400)

    conversation_history.append({"role": "user", "content": final_command})


    try:
        # Send the dynamic command to OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history,
            ##store= true,
        )
        assistant_response = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": assistant_response})
        request.session['conversation_history'] = conversation_history

        return JsonResponse({"response": assistant_response})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

