import { create } from 'zustand';

export type ArticleCTA = {
  label: string;
  explanation: string;
};

export type ArticleSource = {
  outlet: string;
  url: string;
  rewriteReason: string;
  model: string;
  status: 'approved' | 'needs_review';
};

export type Article = {
  id: string;
  title: string;
  excerpt: string;
  category: string;
  publishedAt: string;
  valuePropTag: string;
  cta: ArticleCTA;
  source: ArticleSource;
};

type ArticlesState = {
  articles: Article[];
  featuredCategory: string;
  setFeaturedCategory: (category: string) => void;
  addArticle: (article: Article) => void;
};

const initialArticles: Article[] = [
  {
    id: 'ops-01',
    title: 'Ops Laugh Lab: How Support Teams Ship Punchlines in 60 Minutes',
    excerpt: 'Checklist-driven humor keeps SLAs predictable while surfacing the original source link and guardrails.',
    category: 'Ops Laugh Lab',
    publishedAt: '2024-05-20',
    valuePropTag: 'Transparency badge',
    cta: {
      label: 'Share checklist',
      explanation: 'Send to Ops Slack with badge + source metadata.',
    },
    source: {
      outlet: 'Reddit /r/operations',
      url: 'https://reddit.com/r/operations/post-123',
      rewriteReason: 'Localized punchline + policy context',
      model: 'LLM-Llama3-8B-Q4',
      status: 'approved',
    },
  },
  {
    id: 'product-01',
    title: 'Product Panic Room: Feature Flags vs. Meme Flags',
    excerpt: 'PMs compare experiment backlogs with industry memes to explain trade-offs to stakeholders.',
    category: 'Product Panic Room',
    publishedAt: '2024-05-20',
    valuePropTag: 'Industry meme',
    cta: {
      label: 'Open brief',
      explanation: 'Preview original context + rewrite rationale.',
    },
    source: {
      outlet: 'Product Hunt commentary',
      url: 'https://www.producthunt.com/posts/ops-lab',
      rewriteReason: 'Added Korean CTA macro referencing value prop test',
      model: 'LLM-Llama3-8B-Q4',
      status: 'approved',
    },
  },
  {
    id: 'marketing-01',
    title: 'Marketing Meme Board: B2B Humor with Proof Links',
    excerpt: 'Ad buyers get template-ready copy that ships with transparency widgets and source macros.',
    category: 'Marketing Meme Board',
    publishedAt: '2024-05-19',
    valuePropTag: 'Partner widget',
    cta: {
      label: 'Book partner session',
      explanation: 'Attach PDF proof showing cost + logs.',
    },
    source: {
      outlet: 'LinkedIn creative ops thread',
      url: 'https://linkedin.com/posts/creative-ops',
      rewriteReason: 'Converted thread to slide macro with CTA stack',
      model: 'LLM-NanoTranslate-13B-Q8',
      status: 'approved',
    },
  },
  {
    id: 'dev-01',
    title: 'Dev Standup Satires: Bug Bash with Punchline Commits',
    excerpt: 'Developers share annotated snippets with transparency badges to keep QA aligned.',
    category: 'Dev Standup Satires',
    publishedAt: '2024-05-18',
    valuePropTag: 'Template reuse',
    cta: {
      label: 'File bug roast',
      explanation: 'Push to Dev channel with KPI tag auto-applied.',
    },
    source: {
      outlet: 'GitHub issue parody',
      url: 'https://github.com/newskoolabs/issues/42',
      rewriteReason: 'Removed user handles + added KPI context',
      model: 'LLM-Llama3-8B-Q4',
      status: 'needs_review',
    },
  },
  {
    id: 'exec-01',
    title: 'Exec Trend Roast: Cost Transparency Beats CPM Inflation',
    excerpt: 'Partners preview cost models, KPI summaries, and CTA defaults per category.',
    category: 'Exec Trend Roast',
    publishedAt: '2024-05-17',
    valuePropTag: 'Proof deck',
    cta: {
      label: 'Download proof deck',
      explanation: 'Delivers partner-ready PDF via transparency export.',
    },
    source: {
      outlet: 'Agency advisory call',
      url: 'https://agency.example.com/newskoolabs-notes',
      rewriteReason: 'Redacted client names + appended badge log',
      model: 'LLM-NanoTranslate-13B-Q8',
      status: 'approved',
    },
  },
  {
    id: 'allhands-01',
    title: 'All-hands Catch-up: Week 20 KPI Pulse',
    excerpt: 'Summaries link to KPI catalog entries and transparency exports for every card.',
    category: 'All-hands Catch-up',
    publishedAt: '2024-05-17',
    valuePropTag: 'Onboarding boost',
    cta: {
      label: 'Share recap',
      explanation: 'Send omni-channel CTA stack snapshot.',
    },
    source: {
      outlet: 'NewsKoo observability deck',
      url: 'https://docs.newskoolabs.dev/phase007',
      rewriteReason: 'Converted analytics memo into card macro',
      model: 'LLM-Llama3-8B-Q4',
      status: 'approved',
    },
  },
];

export const useArticlesStore = create<ArticlesState>((set) => ({
  articles: initialArticles,
  featuredCategory: 'Ops Laugh Lab',
  setFeaturedCategory: (category) => set({ featuredCategory: category }),
  addArticle: (article) =>
    set((state) => ({
      articles: [...state.articles, article],
    })),
}));
