from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

neighborhoods = [
    {"name": "Jamaica Plain", "population": 41012, "distance_from_subway": 0.9, "income": 74198, "growth_rate": 0.015, "transit_dep": 0.40, "feasibility": 0.85,
    "cost_estimate": 350, "distance_from_downtown": 3.8, "modes": [
        {"type": "surface", "feasibility": 0.85, "cost": 350},
        {"type": "tunnel", "feasibility": 0.6, "cost": 700}  
      ]
    },
    {"name": "Hyde Park", "population": 29219, "distance_from_subway": 2.2, "income": 57080, "growth_rate": 0.007, "transit_dep": 0.35, "feasibility": 0.8,
    "cost_estimate": 120, "distance_from_downtown": 7.5, "modes": [
        {"type": "surface", "feasibility": 0.8, "cost": 120},
        {"type": "commuter_upgrade", "feasibility": 0.85, "cost": 100}
      ]
    },
    {"name": "Allston", "population": 28621, "distance_from_subway": 0.8, "income": 37638, "growth_rate": 0.010, "transit_dep": 0.80, "feasibility": 0.9, 
    "cost_estimate": 200, "distance_from_downtown": 3.6, "modes": [
        {"type": "ring", "feasibility": 0.85, "cost": 200},
        {"type": "surface", "feasibility": 0.75, "cost": 300},
        {"type": "tunnel", "feasibility": 0.6, "cost": 800}
      ] 
    },
    {"name": "Brighton", "population": 48330, "distance_from_subway": 1.1, "income": 50291, "growth_rate": 0.008, "transit_dep": 0.50, "feasibility": 0.9,
        "cost_estimate": 200, "distance_from_downtown": 4.9, "modes": [
            {"type": "ring", "feasibility": 0.85, "cost": 200},
            {"type": "surface", "feasibility": 0.75, "cost": 300} 
          ]
        },
        {"name": "Mission Hill", "population": 15883, "distance_from_subway": 0.7, "income": 33432, "growth_rate": 0.005, "transit_dep": 0.60, "feasibility": 0.75,
        "cost_estimate": 60, "distance_from_downtown": 2.7, "modes": [
            {"type": "ring", "feasibility": 0.85, "cost": 200},
            {"type": "surface", "feasibility": 0.7, "cost": 250}
          ]
        },
        {"name": "Roxbury", "population": 24100, "distance_from_subway": 1.3, "income": 27051, "growth_rate": 0.012, "transit_dep": 0.70, "feasibility": 0.7,
        "cost_estimate": 850, "distance_from_downtown": 2.0, "modes": [
            {"type": "ring", "feasibility": 0.8, "cost": 200},
            {"type": "tunnel", "feasibility": 0.7, "cost": 850}
          ]
        },
        {"name": "Mattapan", "population": 27335, "distance_from_subway": 1.5, "income": 43532, "growth_rate": 0.009, "transit_dep": 0.60, "feasibility": 0.8,
        "cost_estimate": 150, "distance_from_downtown": 5.5, "modes": [
            {"type": "ring", "feasibility": 0.8, "cost": 200},
            {"type": "surface", "feasibility": 0.7, "cost": 250} 
          ]
        },
        {"name": "South Boston", "population": 32547, "distance_from_subway": 0.7, "income": 67012, "growth_rate": 0.018, "transit_dep": 0.45, "feasibility": 0.65,
        "cost_estimate": 700, "distance_from_downtown": 1.7, "modes": [
            {"type": "ring", "feasibility": 0.7, "cost": 200},
            {"type": "surface", "feasibility": 0.65, "cost": 700}
          ]
        },
        {"name": "North End", "population": 4277, "distance_from_subway": 0.3, "income": 128022, "growth_rate": 0.003, "transit_dep": 0.30, "feasibility": 0.3,
        "cost_estimate": 700, "distance_from_downtown": 0.8, "modes": [
            {"type": "tunnel", "feasibility": 0.3, "cost": 700}
          ]
        },
        {"name": "East Boston", "population": 41680, "distance_from_subway": 1.2, "income": 49549, "growth_rate": 0.014, "transit_dep": 0.60, "feasibility": 0.6,
        "cost_estimate": 300, "distance_from_downtown": 2.7, "modes": [
            {"type": "ring", "feasibility": 0.7, "cost": 200},
            {"type": "surface", "feasibility": 0.6, "cost": 300}
          ]
        },
        {"name": "Charlestown", "population": 17052, "distance_from_subway": 0.9, "income": 89105, "growth_rate": 0.010, "transit_dep": 0.40, "feasibility": 0.5,
        "cost_estimate": 650, "distance_from_downtown": 1.6, "modes": [
            {"type": "ring", "feasibility": 0.7, "cost": 200},
            {"type": "tunnel", "feasibility": 0.5, "cost": 650}
          ]
        },
        {"name": "Roslindale", "population": 30170, "distance_from_subway": 1.6, "income": 61099, "growth_rate": 0.006, "transit_dep": 0.45, "feasibility": 0.85,
        "cost_estimate": 100, "distance_from_downtown": 5.8, "modes": [
            {"type": "surface", "feasibility": 0.85, "cost": 100},
            {"type": "commuter_upgrade", "feasibility": 0.9, "cost": 80}
          ] 
        },
        {"name": "West Roxbury", "population": 27163, "distance_from_subway": 2.0, "income": 82421, "growth_rate": 0.005, "transit_dep": 0.30, "feasibility": 0.75,
        "cost_estimate": 130, "distance_from_downtown": 7.1, "modes": [
            {"type": "surface", "feasibility": 0.75, "cost": 130},
            {"type": "commuter_upgrade", "feasibility": 0.8, "cost": 90}
          ]
        },
        {"name": "Hyde Park", "population": 29219, "distance_from_subway": 2.2, "income": 57080, "growth_rate": 0.007, "transit_dep": 0.35, "feasibility": 0.8,
        "cost_estimate": 120, "distance_from_downtown": 7.5, "modes": [
            {"type": "surface", "feasibility": 0.8, "cost": 120},
            {"type": "commuter_upgrade", "feasibility": 0.85, "cost": 100}
          ]
        },
        {"name": "South End", "population": 26779, "distance_from_subway": 0.4, "income": 50000, "growth_rate": 0.016, "transit_dep": 0.40, "feasibility": 0.6, 
        "cost_estimate": 600, "distance_from_downtown": 1.0, "modes": [
            {"type": "ring", "feasibility": 0.75, "cost": 200},
            {"type": "surface", "feasibility": 0.6, "cost": 600}
          ]
        }
]

SCENARIO_WEIGHTS = {
    "climate_focus": {"transit_dep": 1.3, "income": 1.2},
    "cost_saving": {"cost_estimate": 2.0, "feasibility": 1.6},
    "growth_focus": {"growth_rate": 1.2, "future_pop": 1.5}
}

DEFAULT_WEIGHTS = {
    "distance": 1.3,
    "population": 1.1,
    "income": 1.0,
    "transit_dep": 0.9,
    "growth_rate": 0.7,
    "feasibility": 1.4,
    "cost_estimate": 1.5,
    "distance_penalty": 0.8,
    "future_pop": 1.2
}

TOTAL_BUDGET = 1500

def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)

def generate_recommendation(projects, scenario, budget):
    if not projects:
        return "No projects could be selected within the budget."

    top_neighborhoods = [p["neighborhood"] for p in projects[:3]]
    mode_counts = {}
    for p in projects:
        mode_counts[p["mode"]] = mode_counts.get(p["mode"], 0) + 1
    dominant_mode = max(mode_counts, key=mode_counts.get)

    return (
        f"Given your budget of ${budget:.0f}M and the {scenario.replace('_', ' ').title()} scenario, "
        f"the model prioritized expansion to {', '.join(top_neighborhoods)}. "
        f"The most commonly selected mode was {dominant_mode}."
    )

def estimate_future_population(n):
    return n["population"] * (1 + n["growth_rate"]) ** 15

def get_total_score(n, feas, cost, future_pop, weights):
    dist_score = normalize(n["distance_from_subway"], 0.2, 2.2) * 10 * weights["distance"]
    pop_score = normalize(n["population"], 15000, 70000) * 10 * weights["population"]
    income_score = (1 - normalize(n["income"], 27000, 130000)) * 10 * weights["income"]
    transit_score = normalize(n["transit_dep"], 0.3, 0.8) * 10 * weights["transit_dep"]
    growth_score = normalize(n["growth_rate"], 0.003, 0.025) * 10 * weights["growth_rate"]
    feas_score = feas * 10 * weights["feasibility"]
    cost_score = (1 - normalize(cost, 60, 1000)) * 10 * weights["cost_estimate"]
    future_pop_score = normalize(future_pop, 15000, 90000) * 10 * weights["future_pop"]

    total = dist_score + pop_score + income_score + transit_score + growth_score + feas_score + cost_score + future_pop_score

    if n.get("distance_from_downtown", 0) > 6 and future_pop < 35000:
        total -= 5 * weights["distance_penalty"]

    return round(total, 2)

def build_all_mode_options(weights):
    options = []
    for n in neighborhoods:
        future_pop = estimate_future_population(n)
        for mode in n["modes"]:
            score = get_total_score(n, mode["feasibility"], mode["cost"], future_pop, weights)
            score_per_cost = score / mode["cost"]
            options.append({
                "neighborhood": n["name"],
                "mode": mode["type"],
                "score": score,
                "cost": mode["cost"],
                "score_per_cost": score_per_cost
            })
    return options

def select_under_budget(options, budget):
    selected = []
    total_cost = 0
    total_score = 0
    seen = set()  # Track (neighborhood, mode) pairs

    for opt in sorted(options, key=lambda x: x["score_per_cost"], reverse=True):
        key = (opt["neighborhood"], opt["mode"])
        if key in seen:
            continue  # skip duplicates

        if total_cost + opt["cost"] <= budget:
            selected.append(opt)
            total_cost += opt["cost"]
            total_score += opt["score"]
            seen.add(key)

    return selected, total_cost, total_score


    for opt in sorted(options, key=lambda x: x["score_per_cost"], reverse=True):
        if total_cost + opt["cost"] <= budget:
            selected.append(opt)
            total_cost += opt["cost"]
            total_score += opt["score"]

    return selected, total_cost, total_score

@app.route("/", methods=["GET", "POST"])
def index():
    selected_projects = []
    total_cost = 0
    total_score = 0
    justification_text = ""
    gap_index_text = ""
    mode_summary_text = ""
    scenario_comparison_text = ""
    recommendation = ""

    if request.method == "POST":
        scenario = request.form.get("scenario", "climate_focus")
        budget = float(request.form.get("budget", 1500))

        weights = DEFAULT_WEIGHTS.copy()
        if scenario in SCENARIO_WEIGHTS:
            weights.update(SCENARIO_WEIGHTS[scenario])

        # Check if user submitted custom weights
        custom_keys = [
            "transit_dep", "income", "growth_rate", "distance",
            "feasibility", "cost_estimate", "population", "future_pop"
        ]
        for key in custom_keys:
            form_key = f"w_{key if key != 'cost_estimate' else 'cost'}"
            val = request.form.get(form_key)
            if val is not None:
                try:
                    weights[key] = float(val)
                except ValueError:
                    pass  # ignore bad input

        all_options = build_all_mode_options(weights)
        selected_projects, total_cost, total_score = select_under_budget(all_options, budget)
        selected_projects.sort(key=lambda x: x["score"], reverse=True)
        recommendation = generate_recommendation(selected_projects, scenario, budget)
        
        justification_lines = []
        neighborhoods_dict = {n["name"]: n for n in neighborhoods}
        for project in selected_projects:
            n = neighborhoods_dict[project["neighborhood"]]
            reasons = []
            if n["transit_dep"] > 0.6:
                reasons.append("high transit dependence")
            if n["growth_rate"] > 0.012:
                reasons.append("strong population growth")
            if project["cost"] < 150:
                reasons.append("low-cost implementation")
            if n["income"] < 45000:
                reasons.append("serves lower-income area")
            if project["mode"] == "ring":
                reasons.append("integrates with new Ring Line")
            if project["score"] > 55:
                reasons.append("overall high strategic value")
            reason_str = ", ".join(reasons) if reasons else "selected for strategic fit"
            justification_lines.append(f"{project['neighborhood']} ({project['mode']}): {reason_str}")
        justification_text = "\n".join(justification_lines)

        # --- Gap Index block ---
        selected_names = set(p["neighborhood"] for p in selected_projects)
        gap_lines = []
        for n in neighborhoods:
            if n["name"] not in selected_names:
                future_pop = estimate_future_population(n)
                need_score = (
                    normalize(n["distance_from_subway"], 0.2, 2.2) * 10 * weights["distance"] +
                    normalize(n["population"], 15000, 70000) * 10 * weights["population"] +
                    (1 - normalize(n["income"], 27000, 130000)) * 10 * weights["income"] +
                    normalize(n["transit_dep"], 0.3, 0.8) * 10 * weights["transit_dep"] +
                    normalize(n["growth_rate"], 0.003, 0.025) * 10 * weights["growth_rate"]
                )
                best_score = max(
                    get_total_score(n, mode["feasibility"], mode["cost"], future_pop, weights)
                    for mode in n["modes"]
                )
                gap = round(need_score - best_score, 2)
                gap_lines.append(f"{n['name']} | Need: {need_score:>5.2f} | Best Mode: {best_score:>5.2f} | Gap: {gap:>5.2f}")
        gap_index_text = "\n".join(gap_lines)

        # --- Mode Summary ---
        mode_summary = {}
        for project in selected_projects:
            mode = project["mode"]
            if mode not in mode_summary:
                mode_summary[mode] = {"count": 0, "total_cost": 0, "total_score": 0}
            mode_summary[mode]["count"] += 1
            mode_summary[mode]["total_cost"] += project["cost"]
            mode_summary[mode]["total_score"] += project["score"]
        mode_summary_lines = []
        for mode, data in mode_summary.items():
            mode_summary_lines.append(f"- {mode}:\n  Projects selected: {data['count']}\n  Total investment: ${data['total_cost']:.0f}M\n  Combined score: {data['total_score']:.2f}")
        mode_summary_text = "\n".join(mode_summary_lines)

        # --- Scenario Comparison ---
        comparison_results = {}
        for scenario_name in ["climate_focus", "cost_saving", "growth_focus"]:
            weights_copy = DEFAULT_WEIGHTS.copy()
            weights_copy.update(SCENARIO_WEIGHTS.get(scenario_name, {}))
            options = build_all_mode_options(weights_copy)
            selected, cost, score = select_under_budget(options, TOTAL_BUDGET)
            comparison_results[scenario_name] = {
                "projects": set((p["neighborhood"], p["mode"]) for p in selected),
                "score": score,
                "cost": cost
            }
        common_projects = set.intersection(*[v["projects"] for v in comparison_results.values()])
        comparison_lines = []
        for name in comparison_results:
            comparison_lines.append(f"{name.replace('_', ' ').title()}: {len(comparison_results[name]['projects'])} projects, ${comparison_results[name]['cost']:.1f}M, Total Score: {comparison_results[name]['score']:.1f}")
        comparison_lines.append("\nCommon Projects Across All Scenarios:")
        comparison_lines.extend([f"- {n} ({m})" for n, m in sorted(common_projects)] if common_projects else ["None"])
        comparison_lines.append("\nUnique Projects by Scenario:")
        for name in comparison_results:
            unique = comparison_results[name]["projects"] - common_projects
            comparison_lines.append(f"{name.replace('_', ' ').title()} only:")
            for proj in sorted(unique):
                comparison_lines.append(f"- {proj[0]} ({proj[1]})")
        scenario_comparison_text = "\n".join(comparison_lines)

    return render_template(
        "index.html",
        projects=selected_projects,
        total_cost=total_cost,
        total_score=total_score,
        justification=justification_text,
        gap_index=gap_index_text,
        mode_summary=mode_summary_text,
        scenario_comparison=scenario_comparison_text, 
        recommendation=recommendation
    )


@app.route("/get_projects", methods=["POST"])
def get_projects():
    data = request.get_json()
    scenario = data.get("scenario", "climate_focus")
    budget = data.get("budget", 1500)

    weights = DEFAULT_WEIGHTS.copy()
    if scenario in SCENARIO_WEIGHTS:
        weights.update(SCENARIO_WEIGHTS[scenario])

    all_options = build_all_mode_options(weights)
    selected_projects, total_cost, total_score = select_under_budget(all_options, budget)

    return jsonify({
        "projects": selected_projects,
        "total_cost": total_cost,
        "total_score": total_score
    })
@app.route("/summary")
def summary():
    return render_template("summary.html")

@app.route("/profile/<name>")
def neighborhood_profile(name):
    readable_name = name.replace('_', ' ').title()
    for n in neighborhoods:
        if n["name"].lower() == readable_name.lower():
            return render_template("profile.html", neighborhood=n)
    return f"No profile found for {readable_name}", 404

@app.route("/methodology")
def methodology():
    return render_template("methodology.html")

@app.route("/compare", methods=["GET", "POST"])
def compare():
    selected_n1 = selected_n2 = None
    comparison_result = None

    if request.method == "POST":
        n1_name = request.form.get("neighborhood1")
        n2_name = request.form.get("neighborhood2")

        n1 = next((n for n in neighborhoods if n["name"] == n1_name), None)
        n2 = next((n for n in neighborhoods if n["name"] == n2_name), None)

        if n1 and n2:
            comparison_result = {"n1": n1, "n2": n2}

    return render_template("compare.html", neighborhoods=neighborhoods, result=comparison_result)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

