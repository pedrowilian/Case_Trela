from typing import List, Optional, Dict, Any
from fuzzywuzzy import fuzz
from src.utils.menu_loader import load_menu
from src.utils.budget_extractor import extract_budget
from src.utils.logger import get_logger
from agents import function_tool

logger = get_logger(__name__)
MENU = load_menu()

@function_tool
def filter_menu(query: str, budget: Optional[float] = None, tags: Optional[List[str]] = None, keywords: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Filter menu items based on query, budget, tags, and keywords with fuzzy matching.

    Args:
        query: User input query.
        budget: Maximum price filter.
        tags: List of dietary or preference tags.
        keywords: List of ingredient or dish type keywords.

    Returns:
        Dictionary with filtered recommendations and user message.
    """
    recommendations_with_scores = []
    debug_filters = {"query": query, "budget": budget, "tags": tags or [], "keywords": keywords or []}
    logger.debug(f"Filtering menu with: {debug_filters}")

    normalized_tags = [t.lower() for t in (tags or [])]
    normalized_keywords = [k.lower() for k in (keywords or [])]

    if not normalized_keywords and query:
        query_words = [
            word for word in query.lower().split()
            if len(word) > 2 and word not in [
                "com", "sem", "até", "para", "o", "a", "os", "as", "um", "uma", "uns", "umas",
                "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas", "por", "porém",
                "mas", "e", "ou", "que", "se", "como", "mais", "menos", "deve", "pode", "ser",
                "ter", "ir", "fazer", "estar"
            ]
        ]
        normalized_keywords.extend(list(set(query_words)))
        logger.debug(f"Extracted keywords from query: {normalized_keywords}")

    for item in MENU:
        score = 0.0
        item_name_lower = item["nome"].lower()
        item_desc_lower = item["descricao"].lower()
        item_tags_lower = [t.lower() for t in item.get("tags", [])]
        search_text = f"{item_name_lower} {item_desc_lower} {' '.join(item_tags_lower)}"

        if budget is not None and item["preco"] > budget:
            logger.debug(f"Skipping '{item['nome']}' (price {item['preco']} > {budget})")
            continue

        if normalized_tags:
            tag_match_count = sum(
                1.0 if n_tag in item_tags_lower else
                0.8 if max((fuzz.ratio(n_tag, i_tag) for i_tag in item_tags_lower), default=0) >= 80 else
                0.5 if any(n_tag in it_tag for it_tag in item_tags_lower) else 0
                for n_tag in normalized_tags
            )
            score += (tag_match_count / len(normalized_tags)) * 0.4 if normalized_tags else 0

        if normalized_keywords:
            keyword_match_count = sum(
                1.0 if fuzz.partial_ratio(n_keyword, item_name_lower) >= 85 else
                0.9 if n_keyword in item_name_lower else
                0.7 if fuzz.partial_ratio(n_keyword, search_text) >= 70 else
                0.5 if n_keyword in search_text else 0
                for n_keyword in normalized_keywords
            )
            score += (keyword_match_count / len(normalized_keywords)) * 0.5 if normalized_keywords else 0

        score += item.get("popularity", 0.5) * 0.1
        if score > 0 or (budget is not None and item["preco"] <= budget and not normalized_tags and not normalized_keywords):
            recommendations_with_scores.append((item, score))

    recommendations_with_scores.sort(key=lambda x: (-x[1], x[0]["preco"]))
    final_recommendations = [
        item for item, score in recommendations_with_scores
        if score >= 0.3 or (not normalized_tags and not normalized_keywords)
    ][:10]

    if "mais barato" in query.lower():
        final_recommendations = sorted(final_recommendations or MENU, key=lambda x: x["preco"])[:1]
        logger.debug(f"Applied 'mais barato' filter: {final_recommendations[0]['nome'] if final_recommendations else 'None'}")

    message_parts = []
    if final_recommendations:
        message_parts.append(f"Encontrei {len(final_recommendations)} prato(s) incrível(is) para você!")
        if any("sem lactose" in t for t in normalized_tags):
            message_parts.append("Todos **sem lactose**, perfeitos para você!")
        if any("vegano" in t for t in normalized_tags):
            message_parts.append("Opções **veganas** cheias de sabor!")
        if any("picante" in t for t in normalized_tags):
            message_parts.append("Com aquele toque **picante** que você ama!")
        if any("saudável" in t for t in normalized_tags) or "saudável" in query.lower():
            message_parts.append("Perfeitos para uma refeição **saudável**!")
        if budget is not None:
            message_parts.append(f"Dentro do seu **orçamento de até R${budget:.2f}**!")
        if "mais barato" in query.lower() and final_recommendations and final_recommendations[0] == sorted(MENU, key=lambda x: x["preco"])[0]:
            message_parts.append("Este é o nosso **prato mais em conta**!")
        message_parts.append("Confira nosso catálogo selecionado com carinho:")
        if any("vegano" in t for t in normalized_tags) or "vegano" in query.lower():
            message_parts.append("Dica: Combine com nossa sobremesa vegana por apenas R$15!")
        final_message = " ".join(message_parts)
    else:
        final_message = (
            f"Hmm, não encontrei nada para '{query}'. "
            "Tente algo como 'prato vegano até R$40', 'algo com frango', ou 'o prato mais barato'. 😊"
        )

    logger.debug(f"Returning {len(final_recommendations)} recommendations with message: {final_message}")
    return {"recommendations": final_recommendations, "message": final_message}

@function_tool
def extract_budget_tool(query: str) -> Optional[float]:
    """Extract numerical budget from user query."""
    return extract_budget(query)