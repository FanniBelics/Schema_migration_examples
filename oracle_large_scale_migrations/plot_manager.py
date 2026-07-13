import json
import pandas as pd
from enums import json_tags, states
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib.patheffects as pe

operation_labels = {
    "migration_migration": "Apply migration",
    "close_migration": "Close migration"
}

phase_labels = {
    "before_migration": "Before migration",
    "in_migration_state": "During migration",
    "after_migration": "After migration"
}


def load_results_as_dataframe(filepath='./oracle_large_scale_migrations/results.json'):
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    rows = []
    for migration_name, steps in data.items():
        for step in steps:
            row = {"migration_name": migration_name, **step}
            rows.append(row)
    
    return pd.DataFrame(rows)

def dml_operations():
    df = load_results_as_dataframe()
    
    df["operation"] = df["step_name"].str.split("_").str[-1]
    df_dml = df[df["operation"].isin(["select", "insert", "update", "delete"])]
    
    migrations = df["migration_name"].unique()

    fig = plt.figure(figsize=(18, 15))
    gs = GridSpec(3, 3, figure=fig, hspace=0.5)

    axes = []
    axes.append(fig.add_subplot(gs[0, 0]))
    axes.append(fig.add_subplot(gs[0, 1]))
    axes.append(fig.add_subplot(gs[0, 2]))
    axes.append(fig.add_subplot(gs[1, 0]))
    axes.append(fig.add_subplot(gs[1, 1]))
    axes.append(fig.add_subplot(gs[1, 2]))
    fig.add_subplot(gs[2, 0]).set_visible(False)  
    axes.append(fig.add_subplot(gs[2, 1]))
    fig.add_subplot(gs[2, 2]).set_visible(False)


    df_dml["phase"] = df_dml["phase"].map(phase_labels)

    phase_order = ["Before migration", "During migration", "After migration"]

    for i, migration in enumerate(migrations):
        subset = df_dml[df_dml["migration_name"] == migration]
    
        sns.barplot(
            data=subset,
            x="operation",
            y="time_cost",
            hue="phase",
            hue_order=phase_order,
            ax=axes[i]
        )
        
        for container in axes[i].containers:
            
            current_max = subset["time_cost"].max()
            axes[i].set_ylim(0, current_max * 1.2)
        
            axes[i].set_title(migration.replace("_", " "), fontsize=8, pad=8)
            axes[i].set_xlabel("")
            axes[i].set_ylabel("Time (seconds)")
            axes[i].legend(fontsize=7)
            axes[i].bar_label(container, fmt="%.1f", fontsize=6, padding=2)

    plt.suptitle("DML cost before vs during vs after migration\n(10,000 records)", fontsize=13)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

def migration_time_costs():
    df = load_results_as_dataframe()
    
    df = df[
        (
            (df["phase"] == states.in_migration_state.value)
            & df["step_name"].str.endswith("migration_migration")
        )
        |
        (
            (df["phase"] == states.after_migration.value)
            & df["step_name"].str.endswith("close_migration")
        )
    ]
    
    df["operation"] = df["step_name"].apply(lambda s: "_".join(s.split("_")[-2:]))
    
    df_migration_steps = df[
        ((df["phase"] == "in_migration_state") & (~df["operation"].isin(["insert", "update", "delete", "select"])))
        |
        ((df["phase"] == "after_migration") & (df["step_name"].str.endswith("close_migration")))
    ]

    fig, ax = plt.subplots(figsize=(14, 6))
    
    df_migration_steps["operation"] = df_migration_steps["operation"].map(operation_labels)

    sns.barplot(
        data=df_migration_steps,
        x="migration_name",
        y="time_cost",
        hue="operation",
        ax=ax
    )
    for container in ax.containers:
        ax.bar_label(container, fmt="%.2f", fontsize=8, padding=2)

    current_max = df_migration_steps["time_cost"].max()
    ax.set_ylim(0, current_max * 1.2)

    ax.set_title("Migration step cost per migration type", fontsize=12)
    ax.set_xlabel("")
    ax.set_ylabel("Time (seconds)")
    ax.set_xticklabels(
        [label.get_text().replace("_", " ") for label in ax.get_xticklabels()],
        rotation=20,
        ha="right",
        fontsize=8
    )

    plt.tight_layout()
    plt.show()

    print(df_migration_steps.head(20))

def main():
    sns.set_theme(style="whitegrid")
    dml_operations()
    migration_time_costs()
    
    
if __name__ == "__main__":
    main()